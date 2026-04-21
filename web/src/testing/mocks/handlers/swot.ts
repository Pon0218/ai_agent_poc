import { HttpResponse, http } from 'msw';

import { env } from '@/config/env';
import { networkDelay } from '../utils';

export const swotHandlers = [
	http.post(`${env.API_URL}/sessions/:session_id/swot/generate`, async () => {
		await networkDelay();

		return HttpResponse.json({
			success: true,
			data: {
				session_id: 'sess_000001',
				status: 'swot_generated',
				swot_markdown:
					'## Strengths\n- 獨特的產品設計，能夠吸引目標客群。\n- 產品網址提供了清晰的資訊，方便消費者了解產品特性。\n- 可能具備良好的品牌形象，增強消費者信任感。\n\n## Weaknesses\n- 產品敘述可能過於簡單，缺乏詳細的功能介紹。\n- 競爭對手可能提供更具吸引力的價格或功能。\n- 網站流量和知名度尚待提升，影響市場滲透率。\n\n## Opportunities\n- 隨著市場需求增加，擴展產品線的潛力大。\n- 可利用數位行銷策略提升品牌曝光率和銷售量。\n- 與其他品牌或影響者合作，增強市場影響力。\n\n## Threats\n- 競爭對手的增多可能導致市場份額下降。\n- 消費者偏好的快速變化可能影響產品的持續吸引力。\n- 經濟不穩定可能影響消費者的購買力。'
			},
			error: null,
			meta: null
		});
	})
];
