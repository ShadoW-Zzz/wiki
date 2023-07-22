import markdown
import random
from django.shortcuts import render
from . import util
mk = markdown.Markdown()

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def md_to_html(title):     
    content = util.get_entry(title)
    if (content == None):
        return None
    else:
        hcontent = mk.convert(content)
        return hcontent

def entry(request, title):
    con = md_to_html(title)
    if con is None:
        return render(request, "encyclopedia/error.html", {"message": "Sorry the content you looking for is not found !!"})
    else:
        return render(request, "encyclopedia/entry.html", {"content": con,"title": title})

def search(request):
    if request.method == "POST":
        search_element = request.POST['q']
        content = util.get_entry(search_element)
        if content:
            html_content = mk.convert(content)
            return render(request, "encyclopedia/entry.html", {"content": html_content, "title": search_element})
        else:
            entries = util.list_entries()
            result = []
            for entry in entries:
                if search_element.lower() in entry.lower():
                    result.append(entry)
            if (len(result) != 0):
                return render(request, "encyclopedia/schrem.html", {"result": result})
            else:
                return render(request, "encyclopedia/error.html", {"message": "Sorry the content you looking for is not found !!"})

def new(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new.html", {"message": "Start Adding your new wiki pages: "})
    elif request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        if util.get_entry(title):
            return render(request, "encyclopedia/error.html", {"message":"This topic already exist"})
        else:
            util.save_entry(title, content)
            return render(request, "encyclopedia/new.html")
        
def random_find(request):
    var = util.list_entries()
    rand = random.choice(var)
    return entry(request, rand)

def edit(request):
    if request.method == "POST":
        title = request.POST["title1"]
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {"title":title, "content": content})

def save_edit(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        util.save_entry(title, content)
        hcontent = md_to_html(title)
    return render(request, "encyclopedia/entry.html", {"title":title, "content":hcontent})