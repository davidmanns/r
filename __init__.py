from py4web import action, URL, redirect


@action("index")
def index():
    redirect(URL("oxcam/registration", scheme=True).replace('/r/', '/'))

@action("<event_id:re:[0-9]*>")
def route(event_id):
    redirect(URL(f"oxcam/registration/{event_id}", scheme=True).replace('/r/', '/'))
