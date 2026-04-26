<script lang="ts">
	import { useCreateSession } from '../hooks/useCreateSession';
	import type { InputType } from '../api/sessions';
	import LoadingState from './LoadingState.svelte';

	let { onSuccess }: { onSuccess: (sessionId: string, productName: string) => void } = $props();

	let productName = $state('');
	let websiteUrl = $state('');
	let productDescription = $state('');
	let submitted = $state(false);

	const mutation = useCreateSession();

	const nameValid = $derived(productName.trim().length > 0);
	const urlValid = $derived(websiteUrl.trim().length > 0);
	const descValid = $derived(productDescription.trim().length > 0);
	const canSubmit = $derived(nameValid && urlValid && descValid && !mutation.isPending);

	function handleSubmit(e: SubmitEvent) {
		e.preventDefault();
		submitted = true;
		if (!canSubmit) return;
		const payload: InputType = {
			product_name: productName,
			website_url: websiteUrl,
			product_description: productDescription
		};
		mutation.mutate(payload, {
			onSuccess: (data) => onSuccess(data.data.session_id, productName)
		});
	}
</script>

{#if mutation.isPending}
	<LoadingState />
{:else}
	<div class="mx-auto max-w-190 px-5 py-[clamp(64px,9vw,120px)] text-center md:px-12">
		<p class="mb-3 font-display text-[clamp(18px,2vw,24px)] text-pl-ink-2 italic">
			Hi, what are you building?
		</p>
		<h1
			class="m-0 mb-16 font-display text-[clamp(36px,5vw,60px)] leading-[1.05] font-semibold tracking-[-0.02em]"
		>
			Drop a URL. Get a full product report.
		</h1>

		<form
			onsubmit={handleSubmit}
			class="rounded-pl-lg bg-pl-card p-2 text-left shadow-[0_1px_0_rgba(0,0,0,0.02)]"
		>
			<div class="border-b px-7 py-5.5" style="border-color: rgba(26,26,24,0.07);">
				<label
					class="mb-2 block font-mono text-[11px] tracking-[0.14em] text-pl-ink-2 uppercase"
					for="f-name"
				>
					產品名稱
					{#if submitted && !nameValid}
						<span
							class="ml-1 font-ui font-normal tracking-normal text-pl-neg normal-case"
							>必填</span
						>
					{/if}
				</label>
				<input
					id="f-name"
					bind:value={productName}
					type="text"
					placeholder="e.g. Notion、Figma、你的 SaaS"
					autocomplete="off"
					class="w-full border-0 bg-transparent py-1 text-[16px] text-pl-ink outline-none placeholder:text-pl-ink-3"
				/>
			</div>

			<div class="border-b px-7 py-5.5" style="border-color: rgba(26,26,24,0.07);">
				<label
					class="mb-2 block font-mono text-[11px] tracking-[0.14em] text-pl-ink-2 uppercase"
					for="f-url"
				>
					產品網址
					{#if submitted && !urlValid}
						<span
							class="ml-1 font-ui font-normal tracking-normal text-pl-neg normal-case"
							>必填</span
						>
					{/if}
				</label>
				<input
					id="f-url"
					bind:value={websiteUrl}
					type="url"
					placeholder="https://example.com"
					autocomplete="url"
					class="w-full border-0 bg-transparent py-1 text-[16px] text-pl-ink outline-none placeholder:text-pl-ink-3"
				/>
			</div>

			<div class="px-7 py-5.5">
				<label
					class="mb-2 block font-mono text-[11px] tracking-[0.14em] text-pl-ink-2 uppercase"
					for="f-desc"
				>
					產品敘述
					{#if submitted && !descValid}
						<span
							class="ml-1 font-ui font-normal tracking-normal text-pl-neg normal-case"
							>必填</span
						>
					{/if}
				</label>
				<textarea
					id="f-desc"
					bind:value={productDescription}
					rows="3"
					placeholder="這個產品解決什麼問題？目標用戶是誰？"
					class="min-h-18 w-full resize-none border-0 bg-transparent py-1 font-ui text-[16px] leading-normal text-pl-ink outline-none placeholder:text-pl-ink-3"
				></textarea>
			</div>

			<div class="flex items-center justify-between px-7 py-4.5">
				<span class="font-mono text-[11px] tracking-widest text-pl-ink-2">
					⏱&nbsp; Avg. analysis · 1m 48s
				</span>
				<button
					type="submit"
					class="inline-flex cursor-pointer items-center gap-2 rounded-full bg-pl-accent px-5 py-3 text-[14px] font-medium text-pl-bg transition-colors hover:bg-pl-accent-h"
				>
					Analyze →
				</button>
			</div>
		</form>

		{#if mutation.isError}
			<p role="alert" class="mt-3 text-[13px] text-pl-neg">
				Something went wrong. Please try again.
			</p>
		{/if}
	</div>
{/if}
