import hanlp
from fastapi import APIRouter, Body
from fastapi.responses import Response
from hanlp.pretrained.ner import MSRA_NER_ELECTRA_SMALL_ZH
from hanlp.pretrained.tok import FINE_ELECTRA_SMALL_ZH

router = APIRouter()


@router.post("/api/tok", name='分词')
async def hanlp_api(document: str = Body(media_type='application/text')):
    HanLP = hanlp.pipeline() \
        .append(hanlp.utils.rules.split_sentence, output_key='sentences') \
        .append(hanlp.load(FINE_ELECTRA_SMALL_ZH), output_key='tok') \
        .append(hanlp.load(MSRA_NER_ELECTRA_SMALL_ZH), output_key='ner', input_key='tok')
    response = HanLP(document)
    return response
