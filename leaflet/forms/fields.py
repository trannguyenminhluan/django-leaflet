from __future__ import unicode_literals

import django

if django.VERSION >= (1, 6, 0):
    from django.contrib.gis.forms.fields import GeometryField as BaseGeometryField
else:
    from django.contrib.gis.forms.fields import GeometryField as BaseField

    class BaseGeometryField(BaseField):  # noqa
        geom_type = 'GEOMETRY'

        def __init__(self, *args, **kwargs):
            kwargs['geom_type'] = self.geom_type
            super(BaseGeometryField, self).__init__(*args, **kwargs)


from .widgets import LeafletWidget


class GeometryField(BaseGeometryField):
    widget = LeafletWidget
    geom_type = 'GEOMETRY'

    def __init__(self, *args, **kwargs):
        super(GeometryField, self).__init__(*args, **kwargs)
        self.widget.geom_type = self.geom_type


class GeometryCollectionField(GeometryField):
    geom_type = 'GEOMETRYCOLLECTION'


class PointField(GeometryField):
    geom_type = 'POINT'


class MultiPointField(GeometryField):
    geom_type = 'MULTIPOINT'


class LineStringField(GeometryField):
    geom_type = 'LINESTRING'


class MultiLineStringField(GeometryField):
    geom_type = 'MULTILINESTRING'


class PolygonField(GeometryField):
    geom_type = 'POLYGON'


class MultiPolygonField(GeometryField):
    geom_type = 'MULTIPOLYGON'
