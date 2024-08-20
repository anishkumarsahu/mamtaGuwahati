from functools import wraps

from mamtaApp.models import Admin


def filter_by_company(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        # Get the admin user from the request
        company = None
        is_super_admin = False
        try:
            admin_user = Admin.objects.get(userID_id=self.request.user.pk)
            user = self.request.user

            if user.groups.filter(name="SuperAdmin").exists():
                is_super_admin = True
            else:
                # Get the company from the admin user
                is_super_admin = False
                try:
                    company = admin_user.companyID
                except:
                    company = None
        except:
            pass
        # print(company)

        # Filter the other tables based on the company
        filtered_data = func(self, *args, **kwargs, company=company, is_super_admin=is_super_admin)
        # print(filtered_data)

        return filtered_data

    return wrapper