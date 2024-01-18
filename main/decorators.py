from sys import platform
from functools import wraps
from django.shortcuts import render


def change_template(win_path):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            # Call the original view function
            response = view_func(request, *args, **kwargs)

            # Check if the original view returned a response with a template
            if isinstance(response, dict):
                if platform == "linux" or platform == "darwin" or platform == "linux2":
                # Update the template name in the context
                    response['template_name'] = win_path.replace("\\", "/")

                # Render the template with the updated context
                    return render(request, response['template_name'], context=response)
            
                else:
                   return view_func() 

        return wrapper

    return decorator