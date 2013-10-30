import unittest
from django.contrib.auth.models import User
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.test.client import Client

class AdminTestMixin(object):

    object_registry = dict()
    
    def setUp(self):
        self.create_objects()

    def register(self,Model,Object):
        '''
        Creates the object_registry Dict for Model-Views who need Objects
        
        '''
        self.object_registry[Model] = Object        
    
    def create_objects(self):
        raise NotImplementedError()
           
    
    def test_admin_views(self):
        '''
        Resolv the Urls from the Admin-object-list and check if the need Object to view the view
        If Yes get the Objects from the Object-registery-dict
        Open the Views and check for Return Code 200
        '''
        test_client = Client()
        for modeladmin in self.get_model_admins(self.models):
            for item in modeladmin.get_urls():
                if item.name.split('_')[-1] in ['change', 'delete', 'history']:
                    obj = self.object_registry[modeladmin.model]
                    self.assertEquals(test_client.get(reverse('admin:'+item.name, args=[obj.id])).status_code,200)
                else:
                    pass
                    self.assertEquals(test_client.get(reverse('admin:'+item.name)).status_code,200)  
           
    def get_model_admins(self, models):
        '''
        Generate Admin Object list by passed Models
        '''
        model_name_list = list()
        admin_list = list()
        
        for k in models:
            model_name_list.append(k.__name__)
        
        admin.autodiscover()
        req = admin.site._registry
        
        for item in req.values():
            if item.model.__name__ in model_name_list:
                admin_list.append(item)
        return admin_list
        
