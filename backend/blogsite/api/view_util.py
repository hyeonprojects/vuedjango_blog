def obj_to_post(obj):
    post = dict(vars(obj))

    if obj.modify_dt:
        post['modify_dt'] = obj.modify_dt.strftime('%Y-%m-%d %H:%M')
    else:
        post['modify_dt'] = ''

    if obj.tags:
        post['tags'] = [tag.name for tag in obj.tags.all()]
    else:
        post['tags'] = []

    if obj.owner:
        post['owner'] = obj.owner.username
    else:
        post['owner'] = 'Anonymous'

    del post['_state']

    return post


def prev_next_post(obj):
    try:
        prevObj = obj.get_prev()
        prevDict = {'id': prevObj.id, 'title': prevObj.title}
    except obj.DoesNotExist:
        prevDict = {}

    try:
        nextObj = obj.get_next()
        nextDict = {'id': nextObj.id, 'title': nextObj.title}
    except obj.DoesNotExist as e:
        nextDict = {}

    return prevDict, nextDict


def make_tag_cloud(qsTag):
    minCount = min(tag.count for tag in qsTag)
    maxCount = max(tag.count for tag in qsTag)

    minWeight, maxWeight = 1, 3

    def get_weight_func(minWeight, maxWeight):
        if minCount == maxCount:
            factor = 1.0
        else:
            factor = (maxWeight - minWeight) / (maxCount - minCount)

        def func(count):
            weight = round(minWeight + (factor * (count - minCount)))
            return weight

        return func

    weight_func = get_weight_func(1, 3)
    tagList = []
    for tag in qsTag:
        weight = weight_func(tag.count)
        tagList.append({
            'name': tag.name,
            'count': tag.count,
            'weight': weight,
        })

    return tagList