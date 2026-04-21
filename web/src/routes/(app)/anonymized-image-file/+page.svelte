<script lang="ts">
	import Photo_library from '@material-symbols/svg-400/outlined/photo_library.svg?component';

	import { useAnonymizedImageFile } from '@/features/anonymiized/hooks/use-anonymized-image-file';
	import Examples from '@/features/anonymiized/components/Examples.svelte';
	import InputPanel from '@/features/anonymiized/components/InputPanel.svelte';
	import AnonMapPanel from '@/features/anonymiized/components/AnonMapPanel.svelte';
	import ResultPanel from '@/features/anonymiized/components/ResultPanel.svelte';
	import LanguageSelector from '@/features/anonymiized/components/LanguageSelector.svelte';
	import ModelSelector from '@/features/anonymiized/components/ModelSelector.svelte';
	import type { InputType } from '@/features/anonymiized/api/anonymized-image-file';
	import {
		customerServiceConversation,
		medicalConsultation,
		legalContract,
		hrRecord
	} from '@/features/anonymiized/assets';

	let image = $state<File | null>(null);
	let input_text = $state('');
	let language = $state<'zh' | 'en'>('zh');
	let model = $state<'gpt-4.1'>('gpt-4.1');
	let fileInput: HTMLInputElement;

	const mutation = useAnonymizedImageFile();

	const examples: Array<{ label: string; text: string; imageUrl: string; filename: string }> = [
		{
			label: '客服對話',
			text: '客服對話範例圖片',
			imageUrl: customerServiceConversation,
			filename: '客服對話.png'
		},
		{
			label: '醫療問診',
			text: '醫療問診範例圖片',
			imageUrl: medicalConsultation,
			filename: '醫療問診.png'
		},
		{
			label: '法律合約',
			text: '法律合約範例圖片',
			imageUrl: legalContract,
			filename: '法律合約.png'
		},
		{
			label: 'HR 紀錄',
			text: 'HR 紀錄範例圖片',
			imageUrl: hrRecord,
			filename: 'HR紀錄.png'
		}
	];

	const MODELS = ['gpt-4.1'] as const;

	let imagePreviewUrl = $derived(image ? URL.createObjectURL(image) : null);
	let charCount = $derived(input_text.length);

	function run() {
		if (!image || mutation.isPending) return;
		const payload: InputType = { image, input_text, language, model };
		mutation.mutate(payload);
	}

	function clear() {
		image = null;
		input_text = '';
		mutation.reset();
		if (fileInput) fileInput.value = '';
	}

	async function applyExample(t: string, imageUrl: string, filename: string) {
		input_text = t;
		mutation.reset();
		const res = await fetch(imageUrl);
		const blob = await res.blob();
		image = new File([blob], filename, { type: blob.type });
		if (fileInput) fileInput.value = '';
	}

	function handleFileChange(e: Event) {
		const file = (e.target as HTMLInputElement).files?.[0];
		if (file) image = file;
	}

	function handleDrop(e: DragEvent) {
		e.preventDefault();
		const file = e.dataTransfer?.files[0];
		if (file && file.type.startsWith('image/')) image = file;
	}
</script>

<p class="w-full text-[14px] leading-5.5 font-light text-s-sub-headline">
	對輸入做敏感資訊匿名化 → 呼叫外部 LLM → guard 驗證 → 反匿名化回傳。
</p>

<!-- ── Examples ───────────────────────────────────────────────────────── -->
<Examples {examples} onselect={(ex) => applyExample(ex.text, ex.imageUrl, ex.filename)} />

<!-- ── Language ───────────────────────────────────────────────────────── -->
<LanguageSelector bind:language />

<!-- ── Model ─────────────────────────────────────────────────────────── -->
<ModelSelector models={MODELS} bind:model />

<!-- ── Two panels ─────────────────────────────────────────────────────── -->
<div class="flex w-full flex-row items-stretch gap-9.25">
	<!-- Input panel -->
	<InputPanel
		{charCount}
		onrun={run}
		onclear={clear}
		isPending={mutation.isPending}
		disabled={mutation.isPending || !image}
	>
		<div class="flex flex-col gap-3 bg-s-card-background p-3">
			<!-- image drop zone -->
			<input
				bind:this={fileInput}
				type="file"
				accept="image/*"
				class="hidden"
				onchange={handleFileChange}
			/>
			<button
				type="button"
				onclick={() => fileInput.click()}
				ondrop={handleDrop}
				ondragover={(e) => e.preventDefault()}
				class="flex h-32 w-full cursor-pointer flex-col items-center justify-center gap-3 rounded-lg border border-dashed border-s-sub-headline bg-s-main transition-opacity hover:opacity-80"
			>
				{#if imagePreviewUrl}
					<img
						src={imagePreviewUrl}
						alt="preview"
						class="h-full w-full rounded-lg object-contain p-1"
					/>
				{:else}
					<Photo_library class="size-6 fill-s-sub-headline" />
					<span class="text-[14px] text-s-sub-headline">加入照片</span>
				{/if}
			</button>

			<!-- textarea -->
			<div class="h-32 bg-s-main">
				<textarea
					bind:value={input_text}
					placeholder="輸入包含敏感資訊的文字，例如：「請幫我查詢王小明的訂單，他的電話是 0912-345-678」"
					class="h-full w-full resize-none overflow-auto bg-s-main p-3 text-[14px] leading-5.25 text-s-background outline-none placeholder:text-s-sub-headline placeholder:opacity-60"
				></textarea>
			</div>
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
