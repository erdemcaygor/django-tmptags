
=====
django-tmptags
=====

A django package that allows check user permissons,check group and query filtering on django models.


Installation
-----------

1. Download and unpack source code and run 'python setup.py install' in main source code directory.

2.Add "tmptags" to your INSTALLED_APPS setting like this.

    INSTALLED_APPS = [
        ...
        'tmptags',
    ]


Usage
-------

-First template tag is 'objfilter' that allows query filtering.

 Example usage:

   {% load objfilter %}
   {% objfilter app='your_app' model='your_model_in_app' name='erdem' user=request.user.id salary__gte=700 as your_object%}

   {% for obj in your_object %}
     .....
   {% endfor %}

-Second template tag is 'checkperm' that allows check user permissions.
 
 Example usage:
 
    {% load ckeckperm %}
    {% checkperm 'permission_name' as can_do %}

    {% if can_do %}
      .....
    {% endif %}

-Last template tag is 'ckeckgroup' that allows ckeck user is member this group.
 
 Example usage:
 
    {% load ckeckgroup %}
    {% ckeckgroup 'group_name' as ismember %}

    {% if ismember %}
      ......
    {% endif %}


