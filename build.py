#top and bottom template, 

def main():
#    top_template = open('templates/top.html').read()
#    bottom_template=open('templates/bottom.html').read()
#   template = open('templates/base.html').read()

    
    
#    middle_template=open('templates/content_index.html').read()
#    index_html = top_template + middle_template + bottom_template
#    open("docs/index.html",'w+').write(index_html)

#    middle_template=open('templates/content_bio.html').read()
#    bio_html = top_template + middle_template + bottom_template
#    open("docs/bio.html",'w+').write(index_html)


#    middle_template=open('templates/content_contact.html').read()
#    contact_html = top_template + middle_template + bottom_template
#    open("docs/contact.html",'w+').write(index_html)

    pages = [
       {   
           "filename": "content/index2.html",
           "output": "docs/index.html",
          "title": "Index About Me",
       },
       {
          "filename": "content/bio2.html",
          "output": "docs/bio.html",
          "title": "My bio",
       },
       {
         "filename": "content/contact2.html",
          "output": "docs/contact.html",
          "title": "My contact",
      },
    ]
     
    for page in pages:
      print(page)
      #page_title = page['title']
      template = open('templates/base.html').read()
      content_filename = page['filename']
      print('this is content_filename', content_filename)
      content = open(content_filename).read()
      finished_page = template.replace("{{Darlacontent}}", content)
      open(page['output'], 'w+').write(finished_page)
      print('done')
    
if __name__ == "__main__":
    main()
    
