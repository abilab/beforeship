from beforeship.settings import PORTAL_URL


def get_portal_url(request):
    return {"PORTAL_URL": PORTAL_URL}
