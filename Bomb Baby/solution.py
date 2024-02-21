def answer(m, f):
  m, f = int(m), int(f)
  count = 0
  while min(m, f) != 1:
		if max(m, f) % min(m, f) == 0:
			return "impossible"
			
		count += max(m, f)/min(m, f)
		(m, f) = (max(m, f)%min(m, f), min(m, f))
  return count + max(m, f) - 1