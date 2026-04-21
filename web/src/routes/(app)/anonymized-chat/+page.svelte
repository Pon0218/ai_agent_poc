<script lang="ts">
	import { useAnonymizedChat } from '@/features/anonymiized/hooks/use-anonymized-chat';
	import Examples from '@/features/anonymiized/components/Examples.svelte';
	import InputPanel from '@/features/anonymiized/components/InputPanel.svelte';
	import AnonMapPanel from '@/features/anonymiized/components/AnonMapPanel.svelte';
	import ResultPanel from '@/features/anonymiized/components/ResultPanel.svelte';
	import LanguageSelector from '@/features/anonymiized/components/LanguageSelector.svelte';
	import ModelSelector from '@/features/anonymiized/components/ModelSelector.svelte';

	let text = $state('');
	let language = $state<'zh' | 'en'>('zh');
	let model = $state('gpt-4.1');

	const mutation = useAnonymizedChat();

	const examples: Array<{ label: string; text: string }> = [
		{
			label: '客服對話',
			text: '您好，我是王小明，手機 0912-345-678，信箱 ming@example.com，請幫我查詢訂單 #A2024-9988 的出貨狀態。'
		},
		{
			label: '醫療問診',
			text: '病患陳美玲，身分證 F234567890，生日 1985/03/22，於 2024年9月5日至台大醫院就診，主治醫師李醫師，診斷為高血壓，處方聯絡電話 02-2312-3456。'
		},
		{
			label: '法律合約',
			text: '甲方：台灣科技股份有限公司（統編 12345678），代表人張志明，與乙方 Google Taiwan GmbH 於 2024年11月15日簽訂本服務合約，合約金額新台幣 500 萬元。'
		},
		{
			label: 'HR 紀錄',
			text: '員工：陳美玲，員工編號 EMP-00123，部門：人力資源，薪資 NT$85,000，入職日期：2023年8月1日，主管：張副理，緊急聯絡人電話 0933-222-111。'
		}
	];

	const MODELS = ['gpt-4.1'];

	function run() {
		if (!text.trim() || mutation.isPending) return;
		mutation.mutate({ text, language, model });
	}

	function clear() {
		text = '';
		mutation.reset();
	}

	function applyExample(t: string) {
		text = t;
		mutation.reset();
	}

	// ── derived ───────────────────────────────────────────────────────────────
	let charCount = $derived(text.length);
</script>

<p class="w-full text-[14px] leading-5.5 font-light text-s-sub-headline">
	對輸入做敏感資訊匿名化 → 呼叫外部 LLM → guard 驗證 → 反匿名化回傳。
</p>

<!-- ── Examples ───────────────────────────────────────────────────────── -->
<Examples {examples} onselect={(ex) => applyExample(ex.text)} />

<!-- ── Language ───────────────────────────────────────────────────────── -->
<LanguageSelector bind:language />

<!-- ── Model ─────────────────────────────────────────────────────────── -->
<ModelSelector models={MODELS} bind:model />

<!-- ── Two panels ─────────────────────────────────────────────────────── -->
<div class="flex h-61 w-full flex-row items-stretch gap-9.25">
	<!-- Input panel -->
	<InputPanel
		{charCount}
		onrun={run}
		onclear={clear}
		isPending={mutation.isPending}
		disabled={mutation.isPending || !text.trim()}
	>
		<div class="flex-1 bg-s-card-background p-3">
			<textarea
				bind:value={text}
				placeholder="輸入包含敏感資訊的文字，例如：「請幫我查詢王小明的訂單，他的電話是 0912-345-678」"
				class="h-full w-full resize-none overflow-auto bg-s-main p-3 text-[14px] leading-5.25 text-s-background outline-none placeholder:text-s-sub-headline placeholder:opacity-60"
			></textarea>
		</div>
	</InputPanel>

	<!-- Anon map panel -->
	<AnonMapPanel mappingTable={mutation.data?.mapping_table ?? {}} />
</div>

<!-- ── Result ─────────────────────────────────────────────────────────── -->
<ResultPanel
	error={mutation.error?.message}
	result={mutation.data?.result}
	mappingTable={mutation.data?.mapping_table}
	deanonymizationOk={mutation.data?.deanonymization_ok ?? true}
	deanonymizationFalseReasons={mutation.data?.deanonymization_false_reasons ?? []}
/>
