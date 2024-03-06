from busqueda import buscarProp
from busqueda import buscarPlaylist
from busqueda import buscarGenero
from busqueda import buscarArtista
from busqueda import buscarAlbun
from busqueda import buscarCancion

from insercion import insertProp
from insercion import insertPlaylist
from insercion import insertAlbum
from insercion import insertGen
from insercion import insertCanciones
from insercion import insertArt

def eliminarProp(codProp):
    if codProp in insertProp[0]:
        while insertProp()[0]!=[]:
            if insertProp()[0]==codProp:
                insertProp()[0].remove([codProp])                
            else:
                continue
            insertProp()[0]=insertProp()[0][1:]
        return (f'La lista actualizada: {insertProp()[0]}, y el elemento eliminado fue: {codProp}')
