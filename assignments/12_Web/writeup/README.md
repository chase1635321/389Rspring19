# Crypto II Writeup

Name: Chase Kanipe
Section: 0201

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Chase Kanipe

## Assignment Writeup

### Part 1 (40 Pts)

The first part was vulnerable to an easy sql injection. In the id field of the url, a ' could be used to close off the previous sql statement, followed by a || so the whole statement can eval to true if the second is true, then ' 1=1 so it evaluates to true. The result is item?id=' ||' 1-1. This produced the flag CMSC389R-{y0u_ar3_th3_SQ1_ninj@}.

### Part 2 (60 Pts)

The first one was a simple <script> alert(); </script>

The second could be exploited with the img tag, and the onerror or onload modules. Using <img onload="alert("hello")"></img> worked.

The third could also be exploited with onerror, by putting onerror='alert("xss")' at the end of the url where the img number would go.

The fourth one can be exploited using '); alert(' because from looking at the timer code it can be seen that this inserts a statement in the middle, closing off and re-opening the timer code.

The fifth one can simply be exploited by changing the signum confirm to javascript:alert("xss")

The sixth one could be exploited with callback. I used the hints for this. You could change the end of the js url to //google.com/jsapi?callback=alert
