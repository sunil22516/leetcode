import collections

FACTOR_COUNTS = {
    0: collections.Counter(),
    1: collections.Counter(),
    2: collections.Counter([2]),
    3: collections.Counter([3]),
    4: collections.Counter([2, 2]),
    5: collections.Counter([5]),
    6: collections.Counter([2, 3]),
    7: collections.Counter([7]),
    8: collections.Counter([2, 2, 2]),
    9: collections.Counter([3, 3]),
}

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # 1. Factor t into primes {2,3,5,7}. If t has any other prime factor, impossible.
        prime_count, is_divisible = self._get_prime_count(t)
        if not is_divisible:
            return "-1"

        # 2. Convert the prime requirement into the smallest multiset of digits.
        #    e.g. 2^6 * 5  ->  {8,8,5}  ->  smallest number "588"
        factor_count = self._get_factor_count(prime_count)
        min_digits_needed = sum(factor_count.values())

        # If we already need more digits than num has, any number with that many
        # digits is automatically > num, so just return the smallest such number.
        if min_digits_needed > len(num):
            return self._construct(factor_count)

        # 3. Compute total prime factors provided by the original num.
        #    If num is zero-free and already covers t, return it.
        prefix_factors = collections.Counter()
        for ch in num:
            prefix_factors += FACTOR_COUNTS[int(ch)]

        first_zero = next((i for i, ch in enumerate(num) if ch == '0'), len(num))

        if first_zero == len(num) and self._is_subset(prime_count, prefix_factors):
            return num

        # 4. Scan right-to-left. Try to keep prefix [0..i-1], increase digit i,
        #    and fill suffix [i+1..end] with the smallest valid digits.
        for i in range(len(num) - 1, -1, -1):
            d = int(num[i])
            prefix_factors -= FACTOR_COUNTS[d]   # remove digit i from prefix
            space_after = len(num) - 1 - i

            # If there's a zero to the left, any change here would still leave
            # that zero in the number, making it invalid. Skip.
            if i > first_zero:
                continue

            for bigger in range(d + 1, 10):
                # primes still needed after we place `bigger` at position i
                remaining = self._subtract(
                    self._subtract(prime_count, prefix_factors),
                    FACTOR_COUNTS[bigger]
                )
                suffix_factors = self._get_factor_count(remaining)
                suffix_len = sum(suffix_factors.values())

                if suffix_len <= space_after:
                    ones = space_after - suffix_len
                    return (
                        num[:i]
                        + str(bigger)
                        + '1' * ones
                        + self._construct(suffix_factors)
                    )

        factor_count = self._get_factor_count(prime_count)
        return '1' * (len(num) + 1 - sum(factor_count.values())) + self._construct(factor_count)


    def _get_prime_count(self, t: int):
        count = collections.Counter()
        for p in (2, 3, 5, 7):
            while t % p == 0:
                t //= p
                count[p] += 1
        return count, t == 1

    def _get_factor_count(self, count: dict) -> dict:
        c2 = count.get(2, 0)
        c3 = count.get(3, 0)
        c5 = count.get(5, 0)
        c7 = count.get(7, 0)

        # 2^3 = 8
        cnt8, rem2 = divmod(c2, 3)
        # 3^2 = 9
        cnt9, cnt3 = divmod(c3, 2)
        # 2^2 = 4
        cnt4, cnt2 = divmod(rem2, 2)

        # Prefer 6 over 2+3
        cnt6 = 0
        if cnt2 == 1 and cnt3 == 1:
            cnt2 = cnt3 = 0
            cnt6 = 1

        if cnt3 == 1 and cnt4 == 1:
            cnt2 = 1
            cnt6 = 1
            cnt3 = cnt4 = 0

        return {
            2: cnt2, 3: cnt3, 4: cnt4, 5: c5,
            6: cnt6, 7: c7, 8: cnt8, 9: cnt9,
        }

    def _construct(self, factors: dict) -> str:
        return ''.join(str(d) * factors[d] for d in range(2, 10))

    def _is_subset(self, a: dict, b: dict) -> bool:
        return all(b.get(k, 0) >= v for k, v in a.items())

    def _subtract(self, a: dict, b: dict) -> dict:
        res = dict(a)
        for k, v in b.items():
            res[k] = max(0, res.get(k, 0) - v)
        return res