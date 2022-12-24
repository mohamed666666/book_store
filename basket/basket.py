
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
            self.basket[p_id]={"price":float(product.price),"quantaty":qty}
        self.sesion.modified=True



