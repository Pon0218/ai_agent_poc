import { describe, it, expect } from 'vitest';
import { buildSegments } from './buildSegments';

describe('buildSegments', () => {
	it('空 table 回傳單一 plain segment', () => {
		const result = buildSegments('hello world', {});
		expect(result).toEqual([{ text: 'hello world' }]);
	});

	it('找到 token 對應詞時拆成三段', () => {
		const result = buildSegments('請問 王小明 今天有空嗎', { '[NAME_1]': '王小明' });
		expect(result).toEqual([
			{ text: '請問 ' },
			{ text: '王小明', token: '[NAME_1]' },
			{ text: ' 今天有空嗎' }
		]);
	});

	it('找不到對應詞時保留原文', () => {
		const result = buildSegments('hello world', { '[NAME_1]': '王小明' });
		expect(result).toEqual([{ text: 'hello world' }]);
	});

	it('同一個詞出現多次，每次都標記', () => {
		const result = buildSegments('王小明 和 王小明 都來了', { '[NAME_1]': '王小明' });
		expect(result).toEqual([
			{ text: '王小明', token: '[NAME_1]' },
			{ text: ' 和 ' },
			{ text: '王小明', token: '[NAME_1]' },
			{ text: ' 都來了' }
		]);
	});

	it('多個 token 同時替換', () => {
		const result = buildSegments('王小明 在 台北 工作', {
			'[NAME_1]': '王小明',
			'[LOC_1]': '台北'
		});
		expect(result).toEqual([
			{ text: '王小明', token: '[NAME_1]' },
			{ text: ' 在 ' },
			{ text: '台北', token: '[LOC_1]' },
			{ text: ' 工作' }
		]);
	});

	it('較長的詞優先匹配，避免被短詞誤切', () => {
		// '王小明' 比 '王小' 長，應該先匹配 '王小明'
		const result = buildSegments('王小明來了', {
			'[NAME_1]': '王小明',
			'[NAME_2]': '王小'
		});
		const tokenSegments = result.filter((s) => s.token);
		expect(tokenSegments[0].token).toBe('[NAME_1]');
		expect(tokenSegments[0].text).toBe('王小明');
	});

	it('orig 會 trim 前後空白', () => {
		const result = buildSegments('王小明來了', { '[NAME_1]': '  王小明  ' });
		expect(result).toContainEqual({ text: '王小明', token: '[NAME_1]' });
	});

	it('空字串 resultText 回傳含空文字的 segment', () => {
		const result = buildSegments('', { '[NAME_1]': '王小明' });
		expect(result).toEqual([{ text: '' }]);
	});
});
