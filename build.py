import os    
import glob

pages = []
all_html_files = glob.glob("content/*.html")

def main():
    for html_file in all_html_files:
        file_path = html_file
        file_name = os.path.basename(file_path)
        name_only, extension = os.path.splitext(file_name)
        pages.append({
            "filename": html_file,
            "title": name_only,
            "output": "docs/" + file_name,
        })
    for page in pages:
        #print(pages)
        from jinja2 import Template
        index_html = open(page['filename']).read()
        template_html = open("templates/base.html").read()
        template = Template(template_html)
        finished_page = template.render(
            title=page['title'],
            content=index_html,
            pages = pages
        )
        open(page['output'], 'w+').write(finished_page)

    print("done")

if __name__ == "__main__":
    main()
