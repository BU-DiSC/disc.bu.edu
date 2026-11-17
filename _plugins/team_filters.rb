# Liquid filter for the Team page: `people | by_year` (most recent first) or
# `people | by_year: "oldest"` (earliest first).
#
# Orders people by their `year` field: the year joined for current members (shown oldest
# first) and the year left for alumni (shown most recent first). `year` may be YYYY or
# YYYY-MM; a bare YYYY comes after every YYYY-MM of the same year, in either order.
# Entries with `pin: true` stay on top, people with the same year keep their order from
# the file, and people without a year go last (also in file order).
#
# An optional `rank` (a number, lower first; default 0) groups people within a section,
# e.g. visiting faculty (1), then visiting PhD students (2), then undergrads (3); each
# group is ordered by year as above.
module Disc
  module TeamFilters
    YEAR = /\A(\d{4})(?:-(\d{1,2}))?/

    def by_year(people, order = "newest")
      return people unless people.is_a?(Array)

      sign = order.to_s == "oldest" ? 1 : -1
      pinned, rest = people.partition { |p| p["pin"] }
      groups = rest.group_by { |p| p["rank"].to_i }.sort_by(&:first).map(&:last)
      pinned + groups.flat_map { |g| sort_group(g, sign) }
    end

    private

    def sort_group(people, sign)
      dated, undated = people.partition { |p| !p["year"].to_s.strip.empty? }
      dated = dated.each_with_index.sort_by do |p, i|
        m = YEAR.match(p["year"].to_s.strip)
        unless m
          Jekyll.logger.warn "Team:", "#{p['name']}: year #{p['year'].inspect} is not YYYY or YYYY-MM"
          next [1, 0, 0, 0, i]
        end
        [0, sign * m[1].to_i, m[2] ? 0 : 1, sign * m[2].to_i, i]
      end.map(&:first)
      dated + undated
    end
  end
end

Liquid::Template.register_filter(Disc::TeamFilters)
