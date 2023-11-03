def strip_comments(strng, markers):
    result = []
    comments = strng.split('\n')
    for comment in comments:
        for marker in markers:
            if marker in comment:
                comment = comment.split(marker)[0].rstrip()
        result.append(comment)
    return '\n'.join(result)


strip_comments(' a #b\nc\nd $e f g', ['#', '$'])
