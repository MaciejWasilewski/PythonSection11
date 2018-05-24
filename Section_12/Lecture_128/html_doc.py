# 139, 140, 141

class Tag:
    def __init__(self, name, contents):
        self.start_tag = '<{0}>'.format(name)
        self.end_tag = '</{0}>'.format(name)
        self.contents = contents

    def __str__(self):
        return "{0.start_tag}{0.contents}{0.end_tag}".format(self)

    def display(self):
        return str(self)


class DocType(Tag):

    def __init__(self):
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" http://www.w3.org/TR/html4/strict.dtd', '')
        self.end_tag = ""


class Head(Tag):

    def __init__(self, tag):
        super().__init__('head', tag.display())


class Body(Tag):
    def __init__(self):
        super().__init__('body', '')
        self._body_contents = []

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self._body_contents.append(new_tag)

    def display(self):
        for tag in self._body_contents:
            self.contents += str(tag)
        return str(self)


class HtmlDoc:

    def __init__(self, head_content):
        self._doc_type = DocType()
        self._head = Head(head_content)
        self._body = Body()

    def add_tag(self, name, contents):
        self._body.add_tag(name, contents)

    def display(self):
        temp = self._doc_type.display()
        temp += '<html>'
        temp += self._head.display()
        temp += self._body.display()
        temp += '</html>'
        return temp


if __name__ == "__main__":
    my_page = HtmlDoc(Tag('title', 'document'))
    my_page.add_tag('h1', 'Main heading')
    my_page.add_tag('h2', 'sub-heading')
    my_page.add_tag('p', 'This will apear on the page')
    with open("test_html.html", 'w') as file:
        print(my_page.display(), file=file)
