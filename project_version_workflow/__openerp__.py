# -*- coding: utf-8 -*-
# © 2016 Pierre Faniel
# © 2016 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    'name': 'Project - Version and Workflow link',
    'category': 'Project',
    'summary': 'Allows to change task step on version state change',
    'website': 'https://www.niboo.be/',
    'version': '9.0.1.0.0',
    'description': '''
Allows to change task step on version state change.
    ''',
    'author': 'Niboo',
    'license': 'AGPL-3',
    'depends': [
        'project_version',
        'project_workflow',
    ],
    'data': [
        'views/version_state_step_link.xml',
        'security/ir.model.access.csv',
    ],
    'images': [
        'static/description/versioning_cover.png',
    ],
    'installable': True,
    'application': False,
}