# https://dmoj.ca/problem/wc18c3j1
# James has a can of leftover paint, containing P(1<=P<=100) litres of the stuff.
# 제임스는 P리터의 페인트가 남아있는 캔을 가지고 있습니다.
# When combined with his boundless collection of bottlecaps_amount, this can result in some high-quality wares.
# 그의 무한한 변뚜껑 컬렉션과 결합하며 고품질 제품이 탄생 할 수 있습니다.
# When a bottlecap is artfully covered with B(1<=B<=100) litres of paint, it turns into a completely legitimate, Pokémon league-certified gym badge!
# 병뚜껑을 B리터의 페인트로 예술 적으로 덮으면 완전히 합법 적인 포켓몬 리그 인증 체육관 배지로 변신 합니다.
# James will produce as many badges as he can using the paint, using exactly B litres each.
# 제임스는 각각 정확히 B리터의 페인트를 사용하여 가능한한 많은 배지를 생산 할 것입니다.
# Pokémon trainers love their gym badges, so each such badge is sure to sell for D(1<=D<=100) Pokédollars.
# 포켓몬 트레이너는 체육관 배지를 좋아하므로 각 배지는 D 포켓달러에 판매됩니다.
# There might still be some extra paint left over, once there's not enough for another complete badge. However, there's no need for it to go to waste - James will sell any remaining paint at a rate of 1 Pokédollar per litre.
# 또 다른 완전한 배지를 만들기에 충분하지 않으면 아직 여분의 페인트가 남아 있을수 있습니다.그러나 그것을 낭비 할 필요는 없습니다. 제임스는 남은 페인트를 리터당 1 포켓달러의 가격으로 판매 할 것입니다.
# How much money will James make for Team Rocket in total, from his sales of badges and leftover paint?
# 제임스는 배지와 남은 페인트 판매로 로켓단을 위해 총 얼마의 돈을 벌 수 있습니까?
# 페인트, 병뚜껑, 체육관 배지 개당 받을 수 있는 포켓 달러 입력 받은 값, 출력 값은 제임스가 만든 포켓 달러의 양

paint_amount = input()
if not paint_amount.isdigit():exit(f"{paint_amount}!= digit")
paint_amount = int(paint_amount)
if not 1<= paint_amount <= 100: exit(f"{paint_amount}의 범위 벗어남")
paint_per_badge = input()
if not paint_per_badge.isdigit(): exit(f"{paint_per_badge}!= digit")
paint_per_badge = int(paint_per_badge)
if not 1 <= paint_per_badge <= 100: exit(f"{paint_per_badge}의 범위 벗어남")
badge_sell_price = input()
if not badge_sell_price.isdigit(): exit(f"{badge_sell_price} != digit")
badge_sell_price = int(badge_sell_price)
if not 1 <= badge_sell_price <= 100: exit(f"{badge_sell_price}의 범위 벗어남")


pokedollars = ((paint_amount // paint_per_badge) * badge_sell_price) + (paint_amount % paint_per_badge)
print(pokedollars)

