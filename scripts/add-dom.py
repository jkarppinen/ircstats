import codecs
import sys
from bs4 import BeautifulSoup

conf_file = 'conf_ircstats.yaml'
if os.path.isfile(conf_file):
    vars = yaml.load(open(conf_file))
else:
    raise StandardError('conf_ircstats.yaml missing')

output_filename = vars['stats'] 
html_doc = codecs.open(output_filename, 'r')
soup = BeautifulSoup(html_doc, 'lxml')
output_file = open(output_filename, 'w')

# noindex, nofollow
soup.head.append("""
    <meta name="robots" content="noindex, nofollow">
""")

# Google AdSense
soup.head.append("""
    <script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
    <script>
      (adsbygoogle = window.adsbygoogle || []).push({
	google_ad_client: """ + vars['google_ad_client'] + """,
	enable_page_level_ads: true
	});
    </script>
""")

# Google Analytics
soup.head.append("""
    <script>
      (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
        (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
      m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
        })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

          ga('create', '""" + vars['ga_id'] + """', 'auto', {'siteSpeedSampleRate' : 100});
            ga('send', 'pageview');

    </script>

""")

output_file.write(soup.prettify(formatter=None, encoding='utf-8'))
output_file.close()
