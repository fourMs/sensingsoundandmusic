\include "../../notation/common.ily"
% The ii–V–I progression in C major, preceded by the tonic.
\score {
  <<
    \new ChordNames \chordmode { c1 d:m g c }
    \new Staff { \clef treble \key c \major \time 4/4
      <c' e' g'>1 <d' f' a'> <g' b' d''> <c' e' g'> \bar "|." }
    \new Lyrics \lyricmode { I ii V I }
  >>
  \layout { \context { \Score \override SpacingSpanner.common-shortest-duration = #(ly:make-moment 1/16) \override SpacingSpanner.spacing-increment = #2.4 } }
}
