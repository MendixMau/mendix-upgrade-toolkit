# Replacements: fixture

| id | status | pattern | replacement | evidence | unchecked | effort | risk | verified | handled |
|---|---|---|---|---|---|---|---|---|---|
| R35 | HIT | React 19 removed API | a newer widget version built for React 19 | widgets/Gantt.mpk 1.0.0 runs /findDOMNode/ in its JavaScript and widget X.Gantt is used 1 time(s) on MyOwn.Home |  | M | breaks at runtime | yes |  |
| R38 | HIT | mx.logger | a version that logs through console | widgets/Gantt.mpk 1.0.0 runs /findDOMNode/ in its JavaScript and widget X.Gantt is used 1 time(s) on MyOwn.Home |  | M | breaks at runtime | yes |  |
