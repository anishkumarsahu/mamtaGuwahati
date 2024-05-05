from functools import wraps

from mamtaApp.models import Admin


def filter_by_company(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        # Get the admin user from the request
        admin_user = Admin.objects.get(userID_id=self.request.user.pk)

        # Get the company from the admin user
        company = admin_user.companyID
        # print(company)

        # Filter the other tables based on the company
        filtered_data = func(self, *args, **kwargs, company=company)
        # print(filtered_data)

        return filtered_data

    return wrapper