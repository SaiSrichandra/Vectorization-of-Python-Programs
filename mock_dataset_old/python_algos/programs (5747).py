#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver  # pylint: disable=E0401
from selenium.webdriver.chrome.options import Options  # pylint: disable=E0401
import os
import pathlib
import re
import sys
import time

PAT_HEADER = re.compile(r"^(```python\n\# for use.*production:\n.*\n```\n)", re.MULTILINE)
PAT_IFRAME = re.compile(r"^(\<iframe\n(?:\s+\S+\n)+\>\<\/iframe\>\n)", re.MULTILINE)
PAT_SOURCE = re.compile(r"\s+src\=\"(\S+)\"")


def get_pyvis_html (
    iframe
    ):
    """
located the HTML file generated by PyVis, if any
    """
    source_html = None
    m_source = PAT_SOURCE.search(iframe)

    if m_source:
        source_html = m_source.group(1)

        if "tmp.fig" not in source_html:
            # the <iframe/> wasn't generated by PyVis
            source_html = None

    return source_html


def render_screenshot (
    source_html,
    source_png,
    ):
    """
use Selenium to render `source_png` from `source_html`
    """
    chrome_path = os.getcwd() + "/chromedriver"
    chrome_options = Options()
    browser = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)

    browser.get(source_html)
    time.sleep(20)

    browser.get_screenshot_as_file(source_png)
    browser.quit()


def replace_pyvis_iframe (
    text,  # pylint: disable=W0621
    parent,  # pylint: disable=W0621
    stem,  # pylint: disable=W0621
    ):
    """
Substitute the generated image from PyVis
    """
    output = []

    for chunk in PAT_IFRAME.split(text):
        m_iframe = PAT_IFRAME.match(chunk)

        if m_iframe:
            iframe = m_iframe.group()
            source_html = get_pyvis_html(iframe)

            if source_html:
                source_png = source_html.replace(".html", ".png")

                try:
                    os.mkdir("{}/{}_files".format(parent, stem))
                except:  # pylint: disable=W0702  # nosec
                    pass

                render_screenshot(
                    "file://{}/examples/{}".format(os.getcwd(), source_html),
                    "{}/{}_files/{}".format(parent, stem, source_png),
                    )

                output.append("![png]({}_files/{})".format(stem, source_png))
            else:
                output.append(chunk)
        else:
            output.append(chunk)

    return "\n".join(output)


def replace_sys_header (
    text,  # pylint: disable=W0621
    stem,  # pylint: disable=W0621
    ):
    """
Replace the `sys.path` header for example notebooks
    """
    output = []

    for chunk in PAT_HEADER.split(text):
        m_iframe = PAT_HEADER.match(chunk)

        if m_iframe:
            header = """
!!! note
    To run this notebook in JupyterLab, load [`examples/{stem}.ipynb`](https://github.com/DerwenAI/pytextrank/blob/main/examples/{stem}.ipynb)

""".format(stem=stem)

            output.append(header)
        else:
            output.append(chunk)

    return "\n".join(output)


if __name__ == "__main__":
    filename = pathlib.Path(sys.argv[1])

    parent = filename.parent
    stem = filename.stem

    text = pathlib.Path(filename).read_text()
    text = replace_sys_header(text, stem)
    #print(text)
    #sys.exit(0)

    text = replace_pyvis_iframe(text, parent, stem)

    with open(filename, "w") as f:
        f.write(text)
