<?php

// This file has been auto-generated by the Symfony Dependency Injection Component for internal use.

if (\class_exists(\ContainerAqzxuvs\appDevDebugProjectContainer::class, false)) {
    // no-op
} elseif (!include __DIR__.'/ContainerAqzxuvs/appDevDebugProjectContainer.php') {
    touch(__DIR__.'/ContainerAqzxuvs.legacy');

    return;
}

if (!\class_exists(appDevDebugProjectContainer::class, false)) {
    \class_alias(\ContainerAqzxuvs\appDevDebugProjectContainer::class, appDevDebugProjectContainer::class, false);
}

return new \ContainerAqzxuvs\appDevDebugProjectContainer([
    'container.build_hash' => 'Aqzxuvs',
    'container.build_id' => '8f257563',
    'container.build_time' => 1636634391,
], __DIR__.\DIRECTORY_SEPARATOR.'ContainerAqzxuvs');
