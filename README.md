### Решение задачи.
<p>Через <b><i>x<sub>ij</sub></i></b> обозначим долю <b><i>i</i></b>-ой компоненты (1 - медь, 2 - цинк, 3 - свинец, 4 - никель) в <b><i>j</i></b>-ом виде сплава (1 - обычный, 2 - специальный, 3 - для художественного литья).</p>
Ограничения:

x<sub>11</sub> + x<sub>21</sub> + x<sub>31</sub> + x<sub>41</sub> = 1

x<sub>12</sub> + x<sub>22</sub> + x<sub>32</sub> + x<sub>42</sub> = 1

x<sub>13</sub> + x<sub>23</sub> + x<sub>33</sub> + x<sub>43</sub> = 1

<p>x<sub>11</sub> &#8805 0, x<sub>21</sub> &#8805 0, x<sub>31</sub> &#8805 0, x<sub>41</sub> &#8805 0</p>

<p>x<sub>12</sub> &#8805 0.7, x<sub>22</sub> &#8805 0.1, x<sub>32</sub> &#8804 0.2, x<sub>42</sub> &#8805 0.04</p>

<p>x<sub>13</sub> &#8805 0.5, x<sub>23</sub> &#8805 0, x<sub>33</sub> &#8804 0.3, x<sub>43</sub> &#8805 0.06</p>

Целевая функция: 

(2 - 0.8x<sub>11</sub> - 0.6x<sub>21</sub> - 0.4x<sub>31</sub> - x<sub>41</sub>) + (3 - 0.8x<sub>12</sub> - 0.6x<sub>22</sub> - 0.4x<sub>32</sub> - x<sub>42</sub>) + (4 - 0.8x<sub>13</sub> - 0.6x<sub>23</sub> - 0.4x<sub>33</sub> - x<sub>43</sub>) -> <b><i>max</i></b>
