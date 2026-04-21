import { HttpResponse, http } from 'msw';

import { env } from '@/config/env';
import { networkDelay } from '../utils';

const mockOutput = {
	result: '圖片內容為一段法律合約文字，內容如下：\n\n「Google Taiwan GmbH 於 2024年11月15日簽訂本服務合約，合約金額新台幣500萬元。」\n\n其中個人資訊（張志明)已經匿名化處理，未顯示真實姓名。',
	llm_output:
		'圖片內容為一段法律合約文字，內容如下：\n\n「Google Taiwan GmbH 於 2024年11月15日簽訂本服務合約，合約金額新台幣500萬元。」\n\n其中個人資訊（[[PERSON_1]])已經匿名化處理，未顯示真實姓名。',
	mapping_table: {
		'[[PERSON_1]]': '張志明'
	},
	deanonymization_applied: true,
	deanonymization_ok: true,
	deanonymization_false_reasons: []
};

export const anonymizedHandlers = [
	http.post(`${env.API_URL}/anonymized-chat`, async () => {
		await networkDelay();

		return HttpResponse.json(mockOutput);
	}),

	http.post(`${env.API_URL}/anonymized-image-file`, async () => {
		await networkDelay();

		return HttpResponse.json(mockOutput);
	})
];
