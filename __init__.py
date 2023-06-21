from py4web import action, URL, redirect


@action("index")
def index():
    redirect(URL("oxcam/registration", scheme=True).replace('/r/', '/'))

@action("153")
def event_153():
    redirect(URL("oxcam/registration", "153", scheme=True).replace('/r/', '/'))

@action("154")
def event_154():
    redirect(URL("oxcam/registration", "154", scheme=True).replace('/r/', '/'))

@action("155")
def event_155():
    redirect(URL("oxcam/registration", "155", scheme=True).replace('/r/', '/'))

@action("156")
def event_156():
    redirect(URL("oxcam/registration", "156", scheme=True).replace('/r/', '/'))

@action("157")
def event_157():
    redirect(URL("oxcam/registration", "157", scheme=True).replace('/r/', '/'))

@action("158")
def event_158():
    redirect(URL("oxcam/registration", "158", scheme=True).replace('/r/', '/'))

@action("159")
def event_159():
    redirect(URL("oxcam/registration", "159", scheme=True).replace('/r/', '/'))
