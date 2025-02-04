{
    'name': 'Gestión de Autoescuela',
    'version': '1.0',
    'summary': 'Módulo para gestionar alumnos, clases y exámenes en una autoescuela.',
    'author': 'Fco Santos Manjón-Cabeza Reales (Alu3534222)',
    'sequence': -100,
    'category': 'Education',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/alumno_views.xml',
        'views/profesor_views.xml',
        'views/clase_practica_views.xml',
        'views/clase_teorica_views.xml',
        'views/examen_teorico_views.xml',
        'views/examen_practico_views.xml',
        'views/menu_views.xml',   # Aquí se definen los menús principales
        'views/menu_actions.xml', # Aquí se asignan acciones a los menús
        'data/demo_data.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
