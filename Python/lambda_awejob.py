# coding: utf-8
import json
import urllib.request
import boto3


def lambda_handler(event, context):
    with urllib.request.urlopen("https://api.github.com/repos/awesome-jobs/vietnam/issues") as resp:  # NOQA
        data = resp.read()
    d = json.loads(data.decode())

    # ff = open('/tmp/issues')
    # d = json.load(ff)
    # ff.close()

    JOBFORMAT = '''<li {style}>{date} <a href="{url}">{title}</a> - {salary}</li>\n'''  # NOQA

    with open('/tmp/index.html', 'w') as f:
        f.write('<html><body>\n')

        f.write('<h1>Awesome Jobboard</h1>\n')
        f.write('<ul>\n')

        for job in d:
            title, url = job['title'], job['html_url']
            style = 'style="color:gold"' if 'python' in title.lower() else ''

            lines = list(filter(None, job['body'].splitlines()))
            try:
                salary = lines[
                    lines.index('## Salary Expectation')+1
                ].strip(' *')
            except (IndexError, ValueError):
                salary = 'UNKNOWN'
            date = job['created_at']
            date = date[:date.index('T')]

            f.write(JOBFORMAT.format(url=url, title=title,
                                     salary=salary, date=date,
                                     style=style))

        f.write('</ul>\n')
        f.write('A <a href="https://pymi.vn">PYMIVN</a> toy product\n')
        f.write('</body></html>\n')

    s3 = boto3.resource('s3')
    bucket = s3.Bucket('aj.pymi.vn')
    bucket.put_object(ACL='public-read',
                      Bucket='aj.pymi.vn',
                      Key='index.html',
                      Body=open('/tmp/index.html').read().encode(),
                      ContentType='text/html; charset=utf-8'
                      )
