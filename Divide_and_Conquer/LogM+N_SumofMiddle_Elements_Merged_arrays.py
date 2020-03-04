def find_median(nums1, nums2):
    total_length = len(nums1) + len(nums2)

    if total_length % 2 == 0:
        return (kth_elelement(total_length//2, nums1, nums2) + kth_elelement((total_length//2)-1, nums2, nums2))/2
    return kth_elelement(total_length//2, nums1, nums2)


def kth_elelement(k, nums1, nums2):

    if len(nums1) == 0:
        return nums2[k]

    if len(nums2) == 0:
        return nums1[k]

    mid1 = len(nums1)//2
    mid2 = len(nums2)//2

    if k > mid1 + mid2:
        if nums1[mid1] > nums2[mid2]:
            return kth_elelement(k - mid2 - 1, nums1, nums2[mid2+1:])
        else:
            return kth_elelement(k - mid1 - 1, nums1[mid1+1:], nums2)

    else:
        if nums1[mid1] > nums2[mid2]:
            return kth_elelement(k, nums1[:mid1], nums2)
        else:
            return kth_elelement(k, nums1, nums2[:mid2])


arr1 = [1, 2, 3, 4]
arr2 = [1, 4]
print(find_median(arr1, arr2))
