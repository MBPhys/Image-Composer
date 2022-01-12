# -*- coding: utf-8 -*-

"""
Created on Fri Oct 29 09:32:34 2021

@author: Marc Boucsein
"""
import numpy as np
from magicgui import magic_factory
from napari_plugin_engine import napari_hook_implementation
import napari.types
from napari.types import  LayerDataTuple
import napari





@magic_factory(layout='vertical', 
               call_button="Compose",
               auto_call=False)                  
def Composer(viewer: 'napari.viewer.Viewer'  ,
    Background: 'napari.layers.Image', Foreground: 'napari.layers.Image') ->LayerDataTuple:
       
    if Background and Foreground is not None:
       Background_img=np.copy(Background.data)
       Foreground_img=np.copy(Foreground.data)
       if Foreground.ndim!=Background.ndim:
          return
       for i in range(Foreground.ndim):
         if Foreground_img.shape[i]>Background_img.shape[i]:
            return 
         #translate_crop=scale * izyx + translate
       izyx= (Foreground.translate - Background.translate) // Background.scale       
       Background_img[tuple(slice(int(round(n,0)), int(round(n+x,0))) for n, x in zip(izyx, Foreground_img.shape))]= Foreground_img
       LayerdataTuple=list(viewer.layers[Background.name].as_layer_data_tuple()) 
       LayerdataTuple[0]= Background_img
       LayerdataTuple[1]['name']=Background.name+'_Compose'
       LayerdataTuple_new=tuple(LayerdataTuple)
       return  LayerdataTuple_new 
    else:
       return
   

@napari_hook_implementation
def napari_experimental_provide_dock_widget():
    return Composer

