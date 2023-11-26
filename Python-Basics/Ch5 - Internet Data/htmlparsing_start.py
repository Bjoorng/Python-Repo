# 
# Example file for parsing and processing HTML
# LinkedIn Learning Python course by Joe Marini
#

from html.parser import HTMLParser

paragraphs = 0

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        print("Comment", data)
        pos = self.getpos()
        print(pos[0], "here's a comment", pos[1])

    def handle_starttag(self, tag, attrs):
        print("Start tag", tag)
        pos = self.getpos()
        print(pos[0], "here's a comment", pos[1])

        global paragraphs
        if tag == "p":
            paragraphs += 1

        if len(attrs) > 0:
            print("Attributes")
            for i in attrs:
                print("\t", i[0], "=", i[1])

    def handle_data(self, data):
        if data.isspace():
            return
        print("Data", data)
        pos = self.getpos()
        print(pos[0], "here's some text", pos[1])

def main():
    # instantiate the parser and feed it some HTML
    parser = MyHTMLParser()
    
    f = open("samplehtml.html")
    if f.mode == "r":
        contents = f.read() # read the entire file
        parser.feed(contents)    

    print("paragraph tags", paragraphs)

if __name__ == "__main__":
    main()
  