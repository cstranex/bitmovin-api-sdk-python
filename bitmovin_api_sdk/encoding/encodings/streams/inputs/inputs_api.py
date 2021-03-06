# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.encoding_stream_input import EncodingStreamInput
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError


class InputsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(InputsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def list(self, encoding_id, stream_id, **kwargs):
        # type: (string_types, string_types, dict) -> EncodingStreamInput
        """Stream Input Analysis Details

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param stream_id: Id of the stream.
        :type stream_id: string_types, required
        :return: List of input analysis details
        :rtype: EncodingStreamInput
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/inputs',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id},
            pagination_response=True,
            type=EncodingStreamInput,
            **kwargs
        )
