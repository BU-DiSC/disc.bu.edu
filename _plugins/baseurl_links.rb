# When the site is built into a subfolder (baseurl, e.g. "/disc.bu.edu" while it is served
# from bu-disc.github.io/disc.bu.edu/), prefix every root-relative link and image in the
# rendered HTML with that folder. Content files can then keep plain "/team" or
# "/assets/img/..." paths. With an empty baseurl (disc.bu.edu, or local preview) this
# does nothing.
module Disc
  module BaseurlLinks
    ATTR = /(\b(?:href|src|action|poster)\s*=\s*["']|url\(\s*["']?|;\s*url=)\/(?!\/)/i

    def self.fix(html, base)
      prefix = base.sub(%r{/+\z}, "")
      skip = prefix.sub(%r{\A/}, "")
      html.gsub(ATTR) do
        lead = Regexp.last_match(1)
        rest = Regexp.last_match.post_match
        # Leave links that relative_url already prefixed alone.
        rest.start_with?("#{skip}/") || rest.start_with?("#{skip}\"") || rest.start_with?("#{skip}'") ? "#{lead}/" : "#{lead}#{prefix}/"
      end
    end
  end
end

Jekyll::Hooks.register [:pages, :documents], :post_render do |doc|
  base = doc.site.config["baseurl"].to_s
  next if base.empty? || base == "/"
  next unless doc.output_ext == ".html" || doc.output.to_s.lstrip.start_with?("<")
  doc.output = Disc::BaseurlLinks.fix(doc.output, base)
end
