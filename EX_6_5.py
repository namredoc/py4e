text = "X-DSPAM-Confidence:    0.8475"
d_dots = text.find(':')
v_sting = text[d_dots +1:]
value = float(v_sting.strip())
print(value)