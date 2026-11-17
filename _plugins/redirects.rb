# Builds meta-refresh pages from _data/redirects.yml.
module Disc
  class RedirectGenerator < Jekyll::Generator
    safe true
    def generate(site)
      (site.data["redirects"] || {}).each do |from, to|
        dir, name = File.split(from.sub(%r{^/}, ""))
        dir = "" if dir == "."
        page = Jekyll::PageWithoutAFile.new(site, site.source, dir, "#{name}.html")
        page.data.merge!("layout" => "default", "title" => "Redirecting…",
                         "redirect_to" => to, "sitemap" => false)
        page.content = %(<p>This page has moved to <a href="#{to}">#{to}</a>.</p>)
        site.pages << page
      end
    end
  end
end
