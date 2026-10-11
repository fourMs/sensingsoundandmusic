\include "../../notation/common.ily"
% The four triads on C: major, minor, diminished, augmented.
\score {
  <<
    \new ChordNames \chordmode { c1 c:m c:dim c:aug }
    \new Staff { \clef treble \key c \major \time 4/4
      <c' e' g'>1 <c' ees' g'> <c' ees' ges'> <c' e' gis'> \bar "|." }
    \new Lyrics \lyricmode { "C major" "C minor" "C diminished" "C augmented" }
  >>
  \layout { \context { \Score \override SpacingSpanner.common-shortest-duration = #(ly:make-moment 1/16) \override SpacingSpanner.spacing-increment = #2.4 } }
}
