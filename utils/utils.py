from functools import wraps

from mamtaApp.models import Admin, StaffUser,Company


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


def filter_by_company_by_def(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        company = None
        is_super_admin = False

        try:
            admin_user = Admin.objects.get(userID_id=request.user.pk)
            user = request.user

            if user.groups.filter(name="SuperAdmin").exists():
                is_super_admin = True
            else:
                is_super_admin = False
                try:
                    company = admin_user.companyID
                except:
                    company = None
        except:
            pass

        # Call the decorated function with additional `company` and `is_super_admin` params
        filtered_data = func(request, *args, **kwargs, company=company, is_super_admin=is_super_admin)

        return filtered_data

    return wrapper


def get_user_company_id(user_id):
    try:
        staff = StaffUser.objects.filter(isDeleted=False, isActive=True,userID_id = user_id).first()
        if staff:
            return staff.companyID.pk, staff

        admin = Admin.objects.filter(isDeleted=False, userID_id = user_id).first()
        if admin:
            return admin.companyID.pk, admin

        else:
            first_company = Company.objects.filter(isDeleted=False).first()
            if first_company:
                return first_company.pk, None # Return the primary key, not the instance itself
            return None, None
    except Exception as e:
        return 1, None

