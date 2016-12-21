ENTRIES = [
    {
        "id": 3,
        "title": "Binary Heaps and Templating with Jinja2",
        "body": "Another big day! We are starting to move past hardcoded HTML (woo) into jinja2 templates. No longer are our view handlers reading straight from fully built individual html pages, now we build those pages as templates and fill in the relevant, requested data. This learning journal for instance. We build the unique data into dictionaries which jinja2 looks through and inserts into templates, and voila a fully built view. And, I haven't gotten to it yet, but we'll have to fully test our views now, with help from pyramid's dummyrequest and webtests TestApp. On top of that we briefly learned about binary heaps and then were asked to implement one. The easy method is to use a python list composition thing, and indeed we used that method. However, I wouldn't call it easy, though it was enjoyable to figure out. ALSO, we chose our projects. Whaddaday.",
        "date": "Dec. 20, 2016"
    },
    {
        "id": 2,
        "title": "Pyramid Views and Routes",
        "body": "Today we moved past vanillaish servers and jumped into python web frameworks, specifically Pyramid. We discussed the tools Pyramid gives you to implement MVC architecture, with view controllers and routes. Setting up the pyramid framework is quite straightforward with the scaffolds they provide, I imagine it'd be horrendous if those weren't available. For now, all of our content is static, but we'll be building our data off of templates soon. After setting up the pyramid app, we pushed it to heroku. As our daily data structure, we were introduced to double ended queses, deques, which allow popping and appending on both ends. They werer simple to implement using the double-linked list under the hood.",
        "date": "Dec. 19, 2016"
    },
    {
        "id": 1,
        "title": "TESTING",
        "body": "T0day we m0ved past vanillaish servers and jumped int0 pyth0n web framew0rks, specifically Pyramid. We discussed the t00ls Pyramid gives y0u t0 implement MVC architecture, with view c0ntr0llers and r0utes. Setting up the pyramid framew0rk is quite straightf0rward with the scaff0lds they pr0vide, I imagine it'd be h0rrend0us if th0se weren't available. F0r n0w, all 0f 0ur c0ntent is static, but we'll be building 0ur data 0ff 0f templates s00n. After setting up the pyramid app, we pushed it t0 her0ku. As 0ur daily data structure, we were intr0duced t0 d0uble ended queses, deques, which all0w p0pping and appending 0n b0th ends. They werer simple t0 implement using the d0uble-linked list under the h00d.",
        "date": "Dec. 18, 2016"
    },
]


def get_entries():
    """Return organized entries."""
    latest = ENTRIES[0]
    left_entries = [entry for idx, entry in enumerate(ENTRIES) if idx % 2]
    right_entries = [entry for idx, entry in enumerate(ENTRIES) if idx > 0 and not idx % 2]
    return {"latest": latest,
            "left_entries": left_entries,
            "right_entries": right_entries}
