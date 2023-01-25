
from store.models import Product

class Basket():

    def __init__(self,request):
        self.sesion=request.session
        basket =self.sesion.get('sesion_key')
        if 'sesion_key' not in request.session:
            basket=self.sesion['sesion_key']={}
        self.basket=basket


    def add(self,product,qty):
        p_id=product.id
        if p_id not in self.basket:
            self.basket[p_id]={"price":float(product.price),"quantaty":int(qty)}
        self.sesion.modified=True

    def delete(self,pid):
        if str(pid) in self.basket:

            del self.basket[str(pid)]
        self.sesion.modified = True






    def get_products(self):
        prods=[]
        qts=[]
        for i in self.basket:
            prods.append(Product.objects.get(id=i))
            qts.append(self.basket[i]["quantaty"])

        return prods,qts



    def __len__(self):
        """
        Get the basket data and count the quantaty of items
        """
        return sum(item['quantaty'] for item in self.basket.values())