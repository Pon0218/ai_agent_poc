<script lang="ts">
	import { Button } from '@/components/ui/button';
</script>

<header
	class="sticky top-0 z-50 border-b border-pl-rule"
	style="background: rgba(245,241,235,0.85); backdrop-filter: saturate(140%) blur(10px); -webkit-backdrop-filter: saturate(140%) blur(10px);"
>
	<div class="mx-auto flex h-17 max-w-7xl items-center justify-between px-5 md:px-12 lg:px-20">
		<a
			href="/"
			class="inline-flex items-center gap-2.5 font-display text-[20px] font-semibold tracking-[-0.01em] text-pl-ink"
		>
			<span
				class="h-5.5 w-5.5 shrink-0 rounded-full"
				style="background: radial-gradient(circle at 35% 35%, #F5F1EB 0 4px, transparent 5px), radial-gradient(circle at 50% 50%, #1A1A18 0 60%, transparent 61%); box-shadow: inset 0 0 0 1px #1A1A18;"
				aria-hidden="true"
			></span>
			<span>ProductLens</span>
		</a>

		<nav class="flex items-center gap-8 text-[14px] text-pl-ink">
			<a
				href="/#features"
				class="hidden opacity-[0.78] transition-opacity hover:opacity-100 md:block"
				>The code</a
			>
			<a
				href="/#pricing"
				class="hidden opacity-[0.78] transition-opacity hover:opacity-100 md:block"
				>Why ProductLens</a
			>
			<a
				href="/#testimonials"
				class="hidden opacity-[0.78] transition-opacity hover:opacity-100 md:block"
				>In the wild</a
			>
			<a
				href="/#how"
				class="hidden opacity-[0.78] transition-opacity hover:opacity-100 md:block"
				>Three steps</a
			>
			<Button href="/analyze" variant="primary" size="md">Get Started →</Button>
		</nav>
	</div>
</header>
