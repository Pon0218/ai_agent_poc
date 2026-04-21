<script lang="ts">
	import { RadioGroup } from '@/components/ui/radio-group';

	const items = [
		{ value: 'zh', label: '中文 zh' },
		{ value: 'en', label: 'English en' }
	];

	let {
		language = $bindable('zh')
	}: {
		language: 'zh' | 'en';
	} = $props();
</script>

<div class="flex flex-row items-center gap-3">
	<span class="text-[14px] tracking-[1.2px] text-s-sub-headline uppercase">語言</span>
	<RadioGroup {items} bind:value={language} />
</div>
