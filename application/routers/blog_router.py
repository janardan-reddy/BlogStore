from fastapi import APIRouter

router= APIRouter(
    prefix= '/blog',
    tags= ['blog']
)

@router.get('')
def getBlog():
    return {
        'data': 'fetching all blogs'
    }

