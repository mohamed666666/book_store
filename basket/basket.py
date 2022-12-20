
class Basket():

    def __init__(self,request):
        self.sesion=request.session
        basket =self.sesion.get('sesion_key')
        if 'sesion_key' not in request.session:
            basket=self.sesion['sesion_key']={}
        self.basket=basket



