def spy_game(nums: list):
  k = ""
  for i in nums:
    if i == 0 or i == 7:
      k+=str(i)

  return True if k.find("007") >=0 else False


spy_game([1,0,2,4,0,5,7])
spy_game([1,7,2,0,4,5,0])