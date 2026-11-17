# Generates Squarespace-compatible tag/category pages:
#   /papers/tag/ACM+SIGMOD, /minipages/tag/Demo, /papers/category/...
# GitHub Pages serves /papers/tag/ACM+SIGMOD from papers/tag/ACM+SIGMOD.html.
module Disc
  class TagPage < Jekyll::PageWithoutAFile
    def initialize(site, coll, kind, tag, items)
      slug = tag.tr(" ", "+")
      super(site, site.source, "#{coll}/#{kind}", "#{slug}.html")
      data.merge!(
        "layout" => "tag", "tag" => tag, "collection_name" => coll,
        "title" => "#{coll == 'papers' ? 'Publications' : 'Demos & project pages'}: #{tag}",
        "back_url" => coll == "papers" ? "/publications" : "/minipages",
        "back_title" => coll == "papers" ? "All publications" : "All demos",
        "sitemap" => false,
        "items" => items.sort_by { |d| -(d.data["order"] || d.date.to_i) }
      )
    end
  end

  class TagPageGenerator < Jekyll::Generator
    safe true
    def generate(site)
      %w[papers minipages].each do |coll|
        docs = site.collections[coll]&.docs || []
        { "tag" => "tags", "category" => "categories" }.each do |kind, field|
          docs.flat_map { |d| Array(d.data[field]) }.uniq.each do |t|
            items = docs.select { |d| Array(d.data[field]).include?(t) }
            site.pages << TagPage.new(site, coll, kind, t, items)
          end
        end
      end
    end
  end
end
